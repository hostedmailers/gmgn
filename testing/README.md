# GMGN Testing Module

This directory contains testing scripts and sample data for the GMGN.AI analysis tool.

## Directory Structure

```
testing/
├── gm_top.py         # Top trader analysis test
├── gmgn.py          # Main GMGN functionality tests
├── gmgn_ps.csv      # Sample data for pump smart analysis
├── gmgn_smart.csv   # Sample data for smart money analysis
└── gmgn.csv        # General test data
```

## Test Files

### 1. gm_top.py
Tests for top trader analysis functionality:
- Token performance metrics
- Trader ranking algorithms
- Data aggregation methods

### 2. gmgn.py
Main test suite covering:
- API integration
- Data processing
- CSV export functionality
- Error handling

## Sample Data

The directory includes several CSV files for testing different aspects of the application:

1. `gmgn.csv`: General test data including:
   - Token metrics
   - Trading volumes
   - Price data

2. `gmgn_ps.csv`: Pump smart analysis data:
   - Pump detection metrics
   - Volume analysis
   - Price movement patterns

3. `gmgn_smart.csv`: Smart money tracking data:
   - Wallet behavior analysis
   - Trading patterns
   - Performance metrics

## Running Tests

To run all tests:
```bash
python -m unittest discover
```

To run specific test files:
```bash
python -m unittest testing/gmgn.py
python -m unittest testing/gm_top.py
```

## Test Coverage

The test suite covers:
- API endpoint functionality
- Data processing accuracy
- Error handling scenarios
- Edge cases
- Performance metrics

## Adding New Tests

When adding new tests:
1. Create appropriate test files
2. Add test data if needed
3. Document test cases
4. Include edge cases
5. Verify error handling

## Test Configuration

Tests use the following configuration:
- Sample API responses
- Mock data
- Test environment variables
- Custom assertions

## Test Categories

1. Unit Tests
   - Individual function testing
   - Module isolation
   - Edge case handling

2. Integration Tests
   - API interaction
   - Data flow
   - Module interaction

3. Performance Tests
   - Response time
   - Data processing speed
   - Resource usage

## Best Practices

When working with tests:
1. Keep test data up to date
2. Document test purposes
3. Maintain test independence
4. Use meaningful assertions
5. Clean up test data

## Debug Information

Test files include debug information:
- Console output
- Error logging
- Performance metrics
- Data validation
